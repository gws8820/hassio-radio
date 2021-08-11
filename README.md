# hassio-radio

``` yaml
// scripts.yaml 추가

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
      entity_id: media_player.shilvister_s_home
      media_content_id: "{{ states('sensor.mbc_fm_url') }}{{states('sensor.mbc_fm_urls')}}"
      media_content_type: music
  icon: mdi:radio
  

//configuration.yaml 추가
  
shell_command:
  radio_mbc_fm: 'python3 /config/www/radio/mbc_fm.py'
  
sensor:
  - platform: command_line
    name: mbc_fm_url
    command: "python3 /config/www/radio/mbc_fm_1.py"
  - platform: command_line
    name: mbc_fm_urls
    command: "python3 /config/www/radio/mbc_fm_2.py"
    
google_assistant:
  project_id: 고유 프로젝트 아이디
  service_account: !include service_account.json
  report_state: true
  exposed_domains:
    - input boolean
    - script
  entity_config:
    script.mbc_fm_default:
      name: MBC 표준 FM
      expose: true 
```
