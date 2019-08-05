# House of Misfits Webhook Repository

This is the Python script and the underlying rules files, that control all of the scheduled webhooks
for the Discord server House of Misfits.

## Quickstart

If you want to see/control which messages go to which messages go which webhooks, and when, head over to 
the [schedules](schedules/) folder.

If you want to see/control what the messages actually say, go to the [rules](rules/) folder.

Messages are built using [Tracery](http://tracery.io) by GalaxyKate. Check out the 
[tutorial](http://www.crystalcodepalace.com/traceryTut.html) to learn more.

## How it works

Every day at midnight (EST), the server creates a new schedule for messages for the day, pulling the
`master` branch from this repository if there is any updates to the rules files, etc.

### Rules

The server uses all of the files in the `/rules` folder to determine messages to send, where to send them, 
and when.



## Making changes

### Prioritizing changes

As mentioned above, the server is set up to pull code every 24 hours.

If a change needs to be applied before midnight, 