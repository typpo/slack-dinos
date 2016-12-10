# slack-dinopix

Get a random image from DinosaurPictures.org in a Slack Channel, with Slack Outgoing WebHooks.  Heavily based on [slack-imgur](https://github.com/juanpabloaj/slack-imgur).

![gif](http://i.imgur.com/pUZq3U3.gif)

## Usage

Create a [Slack Outgoing WebHooks][webhook], select a channel, set a trigger word and add [slack-dinopix.herokuapp.com][slack-imgur] to URL(s) field.

![img](http://i.imgur.com/79u5e7L.png)

### Call a random image

Call a random image (if you set `dino` as trigger word)

    dino

### Tag filter

Get a random image tagged with the tag called trex

    dino trex

## Run in your server

Clone the repository and run gunicorn

    gunicorn app:app --log-file=- --reload -b address:port

[webhook]: https://getscreenshots.slack.com/services/new/outgoing-webhook
