# Zoo Animal Image Classification

## Overview

This repository contains code and resources for an API which provides animal image recognition using the GPT-4-Vision model, a powerful IR model developed by OpenAI. The goal of this project is to leverage the capabilities of GPT-4-Vision for extracting animal information from images of animal.

## Images and input form

The user can run this API on any animal image of choosing, by dropping the JPG file in the `animal_images` folder

Here are a few default images

![peacock](https://github.com/immanuel-rajadurai/zoo-img-classifier/assets/91907788/dd129876-894c-4b3a-958a-fcf13aacc33c)

![meerkat](https://github.com/immanuel-rajadurai/zoo-img-classifier/assets/91907788/0b060958-dc37-4290-842c-bb89bc99150e)

![hippo](https://github.com/immanuel-rajadurai/zoo-img-classifier/assets/91907788/04e558e2-5114-4932-9413-f52e002692b2)

## Instructions

1) Add the image of your animal to the `animal_images` folder

2) Import the `ImageRec` class
   
`from image_rec import ImageRec`

3) Create an `ImageRec` object and include the name of the image file you provided

`animal_image_recogniser = ImageRec("mandrill.jpg")`

4) Run the recognition sequence
   
`animal_image_recogniser.recognise()`

5) The output information will display

   ![image](https://github.com/immanuel-rajadurai/zoo-img-classifier/assets/91907788/074d76f7-b435-4e88-aa13-5a39ddeaa8ba)







