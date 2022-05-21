# LPG

#### Introduction

Hello! I'm Lyagva and I "made" this pack!
Well, actually I wasn't making all gradients. I just used gradients from "uiGradients" collection and then, through
code, made "Eyedrop" styled gradient files.

#### Files

There are some folders in "gradients/". They're called "len<n>", where n is length of gradient

#### How to use

How to use this pack:

1. Open ableton and create midi track
2. Put some notes or make 1-color animations
3. Launch "Eyedrop" plugin, switch to "Gradient Edit" tab near "Build Gradient" button
4. Select midi notes, you want to apply gradient at
5. Click "Load &
   Swap" button above "Gradient Edit" button
6. Select file:
   7.1. (if you have gradient already applied) Yay!
   7.2. (if gradient didn't applied) switch back on "New Gradient" tab and click "Build Gradient" button

#### Commentary

I updated my algorythm to find launchpad colors, so gradients should look better now.
If anyone is interested, I take HSV values of every color, find their "distance" like "(h1 - h2) ** 2 * k", where k different for every value
k: h * 0.475, s * 0.2875, v * 0.2375
Found it here: idk, I just have this message:

```

Also, if it helps anyone else... I found the best results in my app when giving HUE a 47.5% importance, SATURATION a 28.75% importance, and BRIGHTNESS a 23.75% importance
```

#### Useful links

uiGradients site: https://uigradients.com
uiGradients source code: https://github.com/Ghosh/uiGradients
Eyedrop: https://www.kaskobi.com/eyedrop
