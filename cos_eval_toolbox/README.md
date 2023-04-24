# COS Evaluation Toolbox

A Python-based concealed object segmentation (COS) evaluation toolbox.

# Features

This repo provides one-key processing for nine evaluation metrics

- MAE
- weighted F-measure
- S-measure
- max/average/adaptive F-measure
- max/average/adaptive E-measure

# One-command evaluation

To evaluate concealed object segmentation (COS) approaches, you should prepare some libraries with the command: `pip install -r requirements.txt`. Then, download benchmark datasets ([OneDrive, 1.16GB](https://anu365-my.sharepoint.com/:u:/g/personal/u7248002_anu_edu_au/EWQU8s3I1cxLvQuYEt2g6gkBO4uwJ2bZq6Vuf9V1Hum7Lg?e=xMMcAr)) and prediction masks ([OneDrive, 4.82GB](https://anu365-my.sharepoint.com/:u:/g/personal/u7248002_anu_edu_au/Edk5mzHO5JNMv0LHDFBdTq4Bgrg_wmsmYg9hjOzh6-nAjw?e=xdVrT4)) just play with this command:

```bash
python eval.py --dataset-json examples_COS/config_cos_dataset_py_example.json \
--method-json examples_COS/config_cos_method_py_example_all.json \
--metric-npy output_COS/cos_metrics.npy \
--curves-npy output_COS/cos_curves.npy \
--record-txt output_COS/cos_results.txt
```

Your results will store at `./cos_eval_toolbox/output_COS/cos_results.txt`


# Custom your evaluation

1. Put your prediction masks into a custom file path like `./benchmark/COS-Benchmarking` and prepare your dataset like `./cos_eval_toolbox/dataset/COD10K/`. Then, generate the Python-style configs via

```bash
python tools/generate_cos_config_files.py
```

2. generate the JSON-style files via

```bash
python tools/info_py_to_json.py -i ./examples_COS -o ./examples_COS
```

3. check files via

```bash
python tools/check_path.py -m examples_COS/config_cos_method_py_example.json -d examples_COS/config_cos_dataset_py_example.json
```

4. start to evaluate

```bash
python eval.py --dataset-json examples_COS/config_cos_dataset_py_example.json \
--method-json examples_COS/config_cos_method_py_example.json \
--metric-npy output_COS/cos_metrics.npy \
--curves-npy output_COS/cos_curves.npy \
--record-txt output_COS/cos_results.txt
```

# Citations

```text
@inproceedings{Fmeasure,
    title={Frequency-tuned salient region detection},
    author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
    booktitle=CVPR,
    number={CONF},
    pages={1597--1604},
    year={2009}
}

@inproceedings{MAE,
    title={Saliency filters: Contrast based filtering for salient region detection},
    author={Perazzi, Federico and Kr{\"a}henb{\"u}hl, Philipp and Pritch, Yael and Hornung, Alexander},
    booktitle=CVPR,
    pages={733--740},
    year={2012}
}

@inproceedings{Smeasure,
    title={Structure-measure: A new way to eval foreground maps},
    author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
    booktitle=ICCV,
    pages={4548--4557},
    year={2017}
}

@inproceedings{Emeasure,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}

@inproceedings{wFmeasure,
  title={How to eval foreground maps?},
  author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
  booktitle=CVPR,
  pages={248--255},
  year={2014}
}
```

# Acknowledgements

This repo is built on [PySODEvalToolkit](https://github.com/lartpang/PySODEvalToolkit). We appreciate Dr Pang for his excellent work, please refer [README.md](https://github.com/lartpang/PySODEvalToolkit/blob/master/readme.md) for more interesting plays. 