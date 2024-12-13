# hassio-radio

Please put python files under /config/www/radio

``` yaml
// scripts.yaml

radio_mbc_default:
  alias: MBC 표준 FM
  sequence:
  - service: shell_command.radio_mbc_fm
  - delay: 00:00:01
  - service: homeassistant.update_entity
    entity_id: sensor.mbc_fm_url
  - service: homeassistant.update_entity
    entity_id: sensor.mbc_fm_urls
  - service: media_player.play_media
    data:
      entity_id: YOUR_ENTITY_ID
      media_content_id: "{{ states('sensor.mbc_fm_url') }}{{ states('sensor.mbc_fm_urls') }}"
      media_content_type: music
  icon: mdi:radio
```

``` yaml
// configuration.yaml
  
shell_command:
  radio_mbc_fm: 'python3 /config/www/radio/mbc_fm.py'
  
sensor:
  - platform: command_line
    name: mbc_fm_url
    command: "python3 /config/www/radio/mbc_fm_1.py"
  - platform: command_line
    name: mbc_fm_urls
    command: "python3 /config/www/radio/mbc_fm_2.py"
```
