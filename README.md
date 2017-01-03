# slack-dinos

Get a random image from DinosaurPictures.org in a Slack Channel, with Slack Outgoing WebHooks.  Heavily based on [slack-imgur](https://github.com/juanpabloaj/slack-imgur).

![pic](https://i.imgur.com/W5HbxaX.png)

## Usage

Create a [Slack Outgoing WebHooks][webhook], select a channel, set a trigger word and add `slack-dinos.herokuapp.com` to URL(s) field.  Kind of like this:

![img](http://i.imgur.com/79u5e7L.png)

### Call a random image

Call a random image (if you set `dino` as trigger word)

    dino
    
## Run in your server

Clone the repository and run gunicorn

    gunicorn app:app --log-file=- --reload -b address:port

[webhook]: https://getscreenshots.slack.com/services/new/outgoing-webhook
