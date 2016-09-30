Colored Buddhabrot Fractal Generator

## Overview

This is a quick script to make colored wallpaper .png images of the Buddhabrot fractal, given the following inputs:
- Height of resulting image
- Width of resulting image
- Red channel number of iterations
- Green channel number of iterations
- Blue channel number of iterations

The Buddhabrot is a special case of the Mandelbrot set, a much-studied fractal investigated in the past century

## What is the Mandelbrot set?

The Mandelbrot set, according to Wikipedia, is "the set of complex numbers c for which the function f_c(z) = z^2 + c does not diverge when iterated from z = 0"

There's a far better explanation of the mathematics on the [Wikipedia page](https://en.wikipedia.org/wiki/Mandelbrot_set), but pretty much, the set checks if a given "c" gives a sequence that's bounded, it ends up in the set. If you programmatically draw what this set looks like, then you can wind up with some nice visualizations of what the set actually looks like:

![Mandelbrot]
[Mandelbrot]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Mandel_zoom_00_mandelbrot_set.jpg/322px-Mandel_zoom_00_mandelbrot_set.jpg

[Source on Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Mandel_zoom_00_mandelbrot_set.jpg/322px-Mandel_zoom_00_mandelbrot_set.jpg)

## How's a Buddhabrot different?

The technique for creating a Buddhabrot involves iterating through options for the complex number "c" used in the Mandelbrot set function.

For a x, y coordinate (pixel) in a rendered Buddhabrot to appear, those x, y coordinates must correspond to at least one complex number which are _not_ a part of the Mandelbrot set, but _do not_ go past some bound within a specified set of iterations. This means that a given "c" causes the Mandelbrot series to grow unbounded towards infinity, but not so fast that it's outside of a picked finite bound for the first few iterations.

Again, for a better explanation of the maths involved, here's the [Wikipedia page](https://en.wikipedia.org/wiki/Buddhabrot).

## So how to render a single Buddhabrot?

First, we make a 2d array of x and y coordinates corresponding to pixels. Each pixel location will have a magnitude (initialized at 0) which will be used to construct a grayscale image later.

For each tested "c" which meets the above criteria, its corresponding pixel's magnitude is increased by 1. This means that brighter portions of the Buddhabrot are x, y coordinates home to many tested complex numbers "c".

Once a set number of iterations have been done, the 2d array has magnitudes ranging from 0-255. This is effectively a portion of a picture! In fact, a grayscale image of this could be made.

Here's an example of one of these grayscale Buddhabrots rendered with 100 iterations:

![GrayBuddhabrot]
[GrayBuddhabrot]: https://github.com/jordanwdunne/buddhabrot-wallpaper/blob/master/grayscaleBuddhabrot.png?raw=true

## Making Colored Buddhabrots

So gray buddhabrots are fun, but you can make colored buddhabrots by combining three grayscale buddhabrots together. While a grayscale image has only one magnitude per pixel, a color photo needs a red, green, and blue magnitude.

To get three separate magnitudes, we can take 3 separate grayscale images, each from renderings with different iteration limits, and then use their magnitudes as the for either the red, green, or blue channels.

The resulting composite image is fully colorized!

![ColorBuddhabrot1]
[ColorBuddhabrot1]: https://github.com/jordanwdunne/buddhabrot-wallpaper/blob/master/3000x2000_7000_400_60_wallpaper.png?raw=true

![ColorBuddhabrot2]
[ColorBuddhabrot2]: https://github.com/jordanwdunne/buddhabrot-wallpaper/blob/master/3000x2000_50_600_5000_wallpaper.png?raw=true

## Experiment!

By adjusting channel colors, different color distributions occur. I've rendered a few (they can take hours), and added them to the repo. They're saved in the form:

widthxheight_redIterations_greenIterations_blueIterations_wallpaper.png

![ColorBuddhabrot3]
[ColorBuddhabrot3]: https://github.com/jordanwdunne/buddhabrot-wallpaper/blob/master/3000x2000_500_60_7000_wallpaper.png?raw=true
