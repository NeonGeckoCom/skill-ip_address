# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ifaddr import get_adapters
from neon_utils.user_utils import get_user_prefs
from requests import get
from adapt.intent import IntentBuilder
from neon_utils.skills.neon_skill import NeonSkill
from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements

from mycroft.skills.core import intent_handler


# TODO: Add something equivalent to neon_utils.net_utils
def get_ifaces(ignore_list=None):
    """ Build a dict with device names and their associated ip address.

    Arguments:
        ignore_list(list): list of devices to ignore. Defaults to "lo"

    Returns:
        (dict) with device names as keys and ip addresses as value.
    """
    ignore_list = ignore_list or ['lo']
    res = {}
    for iface in get_adapters():
        # ignore "lo" (the local loopback)
        if iface.ips and iface.name not in ignore_list:
            for addr in iface.ips:
                if addr.is_IPv4:
                    res[iface.nice_name] = addr.ip
                    break
    return res


class IPSkill(NeonSkill):
    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(network_before_load=False,
                                   internet_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=True,  # TODO: Refactor to handle no internet
                                   requires_network=True,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=False,
                                   no_gui_fallback=True)

    @intent_handler(IntentBuilder("IPIntent").require("query").require("IP")
                    .optionally("public"))
    def handle_query_ip(self, message):
        """
        Handle a user request for the IP Address
        :param message: Message associated with request
        """
        if message.data.get("public"):
            public = True
            addr = {'public': self._get_public_ip_address()}
        else:
            public = False
            addr = get_ifaces()

        dot = self.dialog_renderer.render("dot")

        if len(addr) == 0:  # No IP Address found
            if not get_user_prefs(message)["response_mode"].get(
                    "limit_dialog"):
                self.speak_dialog("no network connection", private=True)
            else:
                self.speak("I'm not connected to a network", private=True)
            return
        if len(addr) == 1:  # Single IP Address to speak
            iface, ip = addr.popitem()
            ip_spoken = ip.replace(".", f" {dot} ")
            if public:
                say_ip = self.translate("word_public")
            else:
                say_ip = self.translate("word_local")
            self.speak_dialog("my address is",
                              {'ip': ip_spoken,
                               'pub': say_ip}, private=True)

            self.gui.show_text(ip, "IP Address")
            return

        for iface in addr:  # Speak and show all Local IP Addresses
            ip = addr[iface]
            self.gui.show_text(ip, iface)

            ip_spoken = ip.replace(".", " " + dot + " ")
            self.speak_dialog("my address on X is Y",
                              {'interface': iface, 'ip': ip_spoken},
                              private=True, wait=True)

    @staticmethod
    def _get_public_ip_address() -> str:
        """
        Get the public IP address associated with the request
        :returns: str public IP address
        """
        # TODO: Server implementation should get this from request origin
        return get('https://api.ipify.org').text
