# <img src='https://0000.us/klatchat/app/files/neon_images/icons/neon_skill.png' card_color="#FF8600" width="50" style="vertical-align:bottom">IP Address

## Summary

Retrieve the [IP address](https://en.wikipedia.org/wiki/IP_address), also known as the "network address" of the Device and respond verbally to the user, and if the Device supports it, display the IP address.

## Requirements

    netifaces==0.10.6

  

Use the following to install if the packages are missing:

    source ${core}/.venv/bin/activate  
    cd ${skills}/ip-address.neon/  
    pip --no-cache-dir install -r requirements.txt

  

## Description

Returns the known IP addresses to the user, if requested. Useful for testing.

## Examples

Say any of the following and wait for Neon to reply with the available list:


* "What's your IP address?"

* "Tell me your IP address."

* "What is my public IP address?"


## Location

    ${skills}/ip-address.neon

## Files
<details>
<summary>Click to expand.</summary>
<br>

    ${skills}/ip-address.neon/requirements.txt  
    ${skills}/ip-address.neon/__init__.py  
    ${skills}/ip-address.neon/test  
    ${skills}/ip-address.neon/test/intent  
    ${skills}/ip-address.neon/test/intent/sample1.intent.json  
    ${skills}/ip-address.neon/test/intent/sample2.intent.json  
    ${skills}/ip-address.neon/test/intent/sample3.intent.json  
    ${skills}/ip-address.neon/settings.json  
    ${skills}/ip-address.neon/dialog  
    ${skills}/ip-address.neon/dialog/es-es  
    ${skills}/ip-address.neon/dialog/es-es/no network connection.dialog  
    ${skills}/ip-address.neon/dialog/es-es/dot.dialog  
    ${skills}/ip-address.neon/dialog/es-es/my address on X is Y.dialog  
    ${skills}/ip-address.neon/dialog/es-es/my address is.dialog  
    ${skills}/ip-address.neon/dialog/sv-se  
    ${skills}/ip-address.neon/dialog/sv-se/no network connection.dialog  
    ${skills}/ip-address.neon/dialog/sv-se/dot.dialog  
    ${skills}/ip-address.neon/dialog/sv-se/my address on X is Y.dialog  
    ${skills}/ip-address.neon/dialog/sv-se/my address is.dialog  
    ${skills}/ip-address.neon/dialog/en-us  
    ${skills}/ip-address.neon/dialog/en-us/no network connection.dialog  
    ${skills}/ip-address.neon/dialog/en-us/dot.dialog  
    ${skills}/ip-address.neon/dialog/en-us/my address on X is Y.dialog  
    ${skills}/ip-address.neon/dialog/en-us/my address is.dialog  
    ${skills}/ip-address.neon/dialog/de-de  
    ${skills}/ip-address.neon/dialog/de-de/no network connection.dialog  
    ${skills}/ip-address.neon/dialog/de-de/dot.dialog  
    ${skills}/ip-address.neon/dialog/de-de/my address on X is Y.dialog  
    ${skills}/ip-address.neon/dialog/de-de/my address is.dialog  
    ${skills}/ip-address.neon/dialog/it-it  
    ${skills}/ip-address.neon/dialog/it-it/no network connection.dialog  
    ${skills}/ip-address.neon/dialog/it-it/dot.dialog  
    ${skills}/ip-address.neon/dialog/it-it/my address on X is Y.dialog  
    ${skills}/ip-address.neon/dialog/it-it/my address is.dialog  
    ${skills}/ip-address.neon/vocab  
    ${skills}/ip-address.neon/vocab/es-es  
    ${skills}/ip-address.neon/vocab/es-es/IP.voc  
    ${skills}/ip-address.neon/vocab/es-es/query.voc  
    ${skills}/ip-address.neon/vocab/sv-se  
    ${skills}/ip-address.neon/vocab/sv-se/IP.voc  
    ${skills}/ip-address.neon/vocab/sv-se/query.voc  
    ${skills}/ip-address.neon/vocab/en-us  
    ${skills}/ip-address.neon/vocab/en-us/IP.voc  
    ${skills}/ip-address.neon/vocab/en-us/query.voc  
    ${skills}/ip-address.neon/vocab/de-de  
    ${skills}/ip-address.neon/vocab/de-de/IP.voc  
    ${skills}/ip-address.neon/vocab/de-de/query.voc  
    ${skills}/ip-address.neon/vocab/it-it  
    ${skills}/ip-address.neon/vocab/it-it/IP.voc  
    ${skills}/ip-address.neon/vocab/it-it/query.voc  
    ${skills}/ip-address.neon/LICENSE  
    ${skills}/ip-address.neon/README.md

</details>


## Class Diagram

[Click Here](https://0000.us/klatchat/app/files/neon_images/class_diagrams/ip-address.png)

## Available Intents
<details>
<summary>Click to expand.</summary>
<br>


### IP.voc

    dirección IP  
    IP  
    dirección de red

  

### query.voc

    qué  
    dime  
    di  
    muestra  
    cuál

  
  

### IP.voc

    ip address  
    ip  
    nätverksaddress

  

### query.voc

    vad  
    vilken  
    berätta  
    säg

  

### IP.voc

    IP address  
    IP  
    network address


### public.voc

    public
    external



### query.voc

    how  
    what  
    tell  
    show

  

### IP.voc

    IP Adresse  
    IP  
    Netzwerkadresse

  

### query.voc

    wie  
    was  
    nenne mir  
    zeige mir

  

### IP.voc

    indirizzo IP  
    IP  
    indirizzo rete

  

### query.voc

    quale  
    dimmi  
    mostra  
    che

</details> 
  

## Details

### Text

        What is my ip address?
        >> I'm at local I.P. address 10 dot 0 dot 0 dot 15
        
        What is my public ip address?
        >> My public network I.P. address is 72 dot 110 dot 150 dot 7


### Picture

### Video

  

## Contact Support

Use the [link](https://neongecko.com/ContactUs) or [submit an issue on GitHub](https://help.github.com/en/articles/creating-an-issue)

## Credits
[Mycroft AI](https://github.com/MycroftAI)
[NeonDaniel](https://github.com/NeonDaniel)
[reginaneon](https://github.com/reginaneon)
Ryan Sipes
Steve Penrod
