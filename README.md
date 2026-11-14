# Spicy Miso Tonkotsu Ramen (`food-picture-01`)

[![make.fun](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/jpereyra243-byte/food-picture-01/rank.svg)](https://make.fun/bounty/food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/jpereyra243-byte/food-picture-01/reward.svg)](https://make.fun/bounty/food-picture-01)

An entry for the make.fun [food-picture-01](https://make.fun/bounty/food-picture-01) competition ("Make the best-looking food picture").

## Overview
- Features an original macro culinary photograph of steaming artisanal Spicy Miso Tonkotsu Ramen in a speckled indigo ceramic bowl: glossy chopstick noodle pull dotted with sesame and chili flakes, charred caramelized pork chashu, two halves of marinated soft-boiled ajitama egg with molten amber yolk, fresh scallions, toasted nori, menma bamboo shoots, and crimson rayu chili oil droplets.
- Standard library Python 3.13 entrypoint validates image completeness (`<= 1 MiB`) and writes deterministically to `/output/entry.png` (`1024 x 1024`, `801,449` bytes).

## Usage
```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
