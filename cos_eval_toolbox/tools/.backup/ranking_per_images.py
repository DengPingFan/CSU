import os
import cv2
import individual_metrics as Measure

model_list = ['2023-arXiv-CamoFormerS', '2023-arXiv-CamoFormerP', '2023-AAAI-HitNet', '2023-arXiv-PopNet', '2022-CVPR-FDNet']

pred_root = '/home/users/u7248002/project/PySODEvalToolkit/cos_benchmark/COS-Benchmarking'
gt_root = '/home/users/u7248002/project/PySODEvalToolkit/cos_benchmark/TestDataset/COD10K/GT'

SM = Measure.Smeasure()
EM = Measure.Emeasure()
MAE = Measure.MAE()

for file_name in os.listdir(gt_root):
    s_list, e_list, r_mae_list, total_list = [], [], [], []
    t_counter = 0
    for model_name in model_list:
        pred_pth = os.path.join(pred_root, model_name, 'COD10K', file_name)
        gt_pth = os.path.join(gt_root, file_name)

        assert os.path.isfile(gt_pth) and os.path.isfile(pred_pth)
        pred_ary = cv2.imread(pred_pth, cv2.IMREAD_GRAYSCALE)
        gt_ary = cv2.imread(gt_pth, cv2.IMREAD_GRAYSCALE)

        assert len(pred_ary.shape) == 2 and  len(gt_ary.shape) == 2 
        if pred_ary.shape != gt_ary.shape:
            pred_ary = cv2.resize(pred_ary, (gt_ary.shape[1], gt_ary.shape[0]), cv2.INTER_NEAREST)
        
        SM.step(pred=pred_ary, gt=gt_ary)
        EM.step(pred=pred_ary, gt=gt_ary)
        MAE.step(pred=pred_ary, gt=gt_ary)

        sm = SM.get_results()['sm']
        em = EM.get_results()['em']['curve'].max()
        r_mae = 1 - MAE.get_results()['mae']

        totol_score = sm + em + r_mae

        s_list.append(sm)
        e_list.append(em)
        r_mae_list.append(r_mae)
        total_list.append(totol_score)
        t_counter += totol_score

    print(f'{file_name} | {total_list[0]} | {total_list[1]} | {total_list[2]} | {total_list[3]} | {total_list[4]} | {t_counter}')