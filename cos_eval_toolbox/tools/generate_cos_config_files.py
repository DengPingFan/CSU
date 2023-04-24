# -*- coding: utf-8 -*-
# @Time    : 2023/4/22
# @Author  : Daniel Ji

import os

def check_integraty():
    """
    Check the matching status of prediction and ground-truth masks
    """
    pred_path = './benchmark/COS-Benchmarking'
    gt_path = './dataset'

    def returnNotMatches(a, b):
        return [[x for x in a if x not in b], [x for x in b if x not in a]]

    for model_name in os.listdir(pred_path):
        for data_name in ['CAMO', 'COD10K', 'NC4K']:
            model_data_path = os.path.join(pred_path, model_name, data_name)
            gt_data_path = os.path.join(gt_path, data_name, 'GT')

            if os.path.exists(model_data_path):
                if not os.listdir(model_data_path) == os.listdir(gt_data_path):
                    info = returnNotMatches(os.listdir(model_data_path), os.listdir(gt_data_path))
                    print('not match', model_name, data_name)
                    print(info)
            else:
                print('not exist', model_name, data_name)


def generate_model_config_py():
    root = './benchmark/COS-Benchmarking'
    write_txt_path = './examples_COS'
    os.makedirs(write_txt_path, exist_ok=True)

    # Open the file in write mode
    with open(f'{write_txt_path}/config_cos_method_py_example_all.py', 'w') as f:
        # Write some data to the file
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('import os\n\n')

        for model_name in os.listdir(root):
            model_path = os.path.join(root, model_name)
            print('{}_root = \"{}\"'.format(model_name.split('-')[-1], model_path))
            f.write('{}_root = \"{}\" \n'.format(model_name.split('-')[-1], model_path))
            print('{} = {{'.format(model_name.split('-')[-1]))
            f.write('{} = {{ \n'.format(model_name.split('-')[-1]))

            for data_name in ['CAMO', 'NC4K', 'COD10K']:
                model_data_path = os.path.join(model_path, data_name)
                if os.path.exists(model_data_path):
                    print('\t\"{}\": dict(path=os.path.join({}_root, \"{}\"), suffix=".png"),'.format(data_name, model_name.split('-')[-1], data_name))
                    f.write('\t\"{}\": dict(path=os.path.join({}_root, \"{}\"), suffix=".png"), \n'.format(data_name, model_name.split('-')[-1], data_name))
                else:
                    print('\t\"{}\": None,'.format(data_name))
                    f.write('\t\"{}\": None, \n'.format(data_name))
            print('}\n')
            f.write('}\n\n')

generate_model_config_py()