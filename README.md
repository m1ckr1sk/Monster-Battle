# Monster-Battle

[![CircleCI](https://circleci.com/gh/m1ckr1sk/Monster-Battle.svg?style=svg)](https://circleci.com/gh/m1ckr1sk/Monster-Battle)

This repo is test project for gathering some thoughts on a configurable set of rules for a rules engine.  

Tests using pytest are hooked to circle ci .  All code **should** be passing in flake 8 and best efforts should be made to use pylint.

An example of how the engine could be used can be seen in the runme.py.  Simply run:

```bash
python runme.py
```

to load the configuration found in configuration_files\basic_config.json.  The example pits the used against a number of monsters
who can be defeated by meeting the criteria set out in the rules.

