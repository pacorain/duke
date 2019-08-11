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

### The Stack

The House of Misfits webhooks system runs on the following technologies:

 - GitHub (you are here!)
 - Jenkins (pulls and runs the code from GitHub)
 - Python (the language telling the computer how to do things)
 - YAML (markup language rules are written in)
 - Tracery (framework for making text dynamic)

Every day at midnight (EST), the Jenkins server creates a new schedule for messages for the day, pulling the
`master` branch from this repository if there is any updates to the rules files, etc.

### Schedules

The server uses all of the files in the `/schedules` folder to determine messages to send, where to send them, 
and when.

Note that it does not matter what file a schedule is in.

#### Syntax

The webhooks system expects each rule file to be in the following syntax:

```yaml
 - message: "#example_rule#" # origin of message to pick from rules
   webhook: webhook_name # defined in webhooks.yml
   schedule: 
     type: hourly # or other supported type
     # schedule syntax depends on type
   
```

#### Supported Types

The following types are currently supported:

 - **weekly**: sends a message at a specific time on a specific day of the week
```yaml
schedule:
  type: weekly
  days: # List of weekdays, i.e. Monday, Tuesday, etc.
    - Monday
    - Tuesday
  time: "14:00" # HH:MM in EST
```
 - **hourly**: sends a message every `interval` hours, starting from 00:00 EST
 ```yaml
schedule:
  type: hourly
  interval: 2 # or other integer
```
 
 - **minutely**: sends a message every `interval` minutes, starting from 00:00 EST
 ```yaml
schedule:
  type: minutely
  interval: 2 # or other integer
```
 
 If another type is needed, [file an issue](https://github.com/pacorain/houseofmisfits/issues/new).



## Making changes

### Prioritizing changes

As mentioned above, the server is set up to pull code every 24 hours.

If a change needs to be applied before midnight, 