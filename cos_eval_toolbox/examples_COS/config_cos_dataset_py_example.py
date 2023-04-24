# -*- coding: utf-8 -*-
import os

_COD_DATA_ROOT = "./dataset"

CAMO = dict(
    root=os.path.join(_COD_DATA_ROOT, "CAMO"),
    image=dict(path=os.path.join(_COD_DATA_ROOT, "CAMO", "Imgs"), suffix=".jpg"),
    mask=dict(path=os.path.join(_COD_DATA_ROOT, "CAMO", "GT"), suffix=".png"),
)

COD10K = dict(
    root=os.path.join(_COD_DATA_ROOT, "COD10K"),
    image=dict(path=os.path.join(_COD_DATA_ROOT, "COD10K", "Imgs"), suffix=".jpg"),
    mask=dict(path=os.path.join(_COD_DATA_ROOT, "COD10K", "GT"), suffix=".png"),
)

NC4K = dict(
    root=os.path.join(_COD_DATA_ROOT, "NC4K"),
    image=dict(path=os.path.join(_COD_DATA_ROOT, "NC4K", "Imgs"), suffix=".jpg"),
    mask=dict(path=os.path.join(_COD_DATA_ROOT, "NC4K", "GT"), suffix=".png"),
)