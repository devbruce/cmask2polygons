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


color_mask_path = '. . .'
color_mask = cv2.cvtColor(cv2.imread(color_mask_path), cv2.COLOR_BGR2RGB)

# Key:str, Val:tuple
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
    pt_type=int,
    add_closept=False,
)
```

### Arguments

- `color_mask`: RGB Image (`numpy.ndarray`)
- `cls_color_map`: Color Value per Class (`dict`)
- `min_area`: Minimum area of object (`float`). Default is 100.0
- `epsilon_param`: Value for polygon approximating (`float`). Default is 8e-4
- `pt_type`: Data type of points. Default is `int`
- `add_closept`: Append end point (== start point) for representing closed. Default is `False`

<br><br>

### Return

- Data type: `dict`
  - Key: Class name (`str`)
  - Value: list of polygon x (`int`), y (`int`) coordinates
