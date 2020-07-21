# cmask2polygons

Convert Color label mask to Polygons per class

<br><br>

## Install

```bash
$ pip install cmask2polygons
```

<br><br>

## How to Use

```python
from cmask2polygons import get_polygons_per_class


IMG_PATH = '. . .'
color_mask = cv2.cvtColor(cv2.imread(IMG_PATH), cv2.COLOR_BGR2RGB)
cls_color_map = {
    "class_name_1": (125, 125, 125),  # RGB Color
    "class_name_2": (70, 20, 225),
    . . .
}

# Get Polygons from Color Label Mask
polygons_per_class = get_polygons_per_class(
    color_mask=color_mask,
    cls_color_map=cls_color_map,
    min_area=100.0,
    epsilon_param=8e-4,
)
```

### Arguments

- `color_mask`: RGB Image (`numpy.ndarray`)
- `cls_color_map`: Color Value per Class (`dict`)
- `min_area`: Minimum area of object (`float`). Default is 100.0
- `epsilon_param`: Value for polygon approximating (`float`). Default is 8e-4

<br><br>

### Return

- Data type: `dict`
  - Key: Class name (`str`)
  - Value: list of polygon x (`int`), y (`int`) coordinates
