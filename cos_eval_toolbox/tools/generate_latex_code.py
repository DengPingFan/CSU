# -*- coding: utf-8 -*-
# @Time    : 2023/4/22
# @Author  : Daniel Ji

eval_txt_path = './output_CDS2K/cos_results.txt'

with open(eval_txt_path) as f:

    model_list, mae_list, maxf_list, avgf_list, adpf_list, maxe_list, avge_list, adpe_list, sm_list, wfm_list, sum_list = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()

    for line in f.readlines():
        if line.startswith('['):
            model = line.split('[')[1].split(']')[0]
            mae = float(line.split('mae: ')[1].split('  ')[0])
            maxf = float(line.split('maxf: ')[1].split('  ')[0])
            avgf = float(line.split('avgf: ')[1].split('  ')[0])
            adpf = float(line.split('adpf: ')[1].split('  ')[0])
            maxe = float(line.split('maxe: ')[1].split('  ')[0])
            avge = float(line.split('avge: ')[1].split('  ')[0])
            adpe = float(line.split('adpe: ')[1].split('  ')[0])
            sm = float(line.split('sm: ')[1].split('  ')[0])
            wfm = float(line.split('wfm: ')[1].split('  ')[0])
            sum = (1-mae) + maxf + avgf + adpf + maxe + avge + adpe + sm + wfm # optional

            print(f'{model}\n&{sm:.3f} &{wfm:.3f} &{mae:.3f} &{adpe:.3f} &{avge:.3f} &{maxe:.3f} &{adpf:.3f} &{avgf:.3f} &{maxf:.3f}')

            model_list.append(model)
            mae_list.append(mae)
            maxf_list.append(maxf)
            avgf_list.append(avgf)
            adpf_list.append(adpf)
            maxe_list.append(maxe)
            avge_list.append(avge)
            adpe_list.append(adpe)
            sm_list.append(sm)
            wfm_list.append(wfm)
            sum_list.append(sum)
    
    # print('\n', max(sm_list), max(wfm_list), min(mae_list), max(adpe_list), max(avge_list), max(maxe_list), max(adpf_list), max(avgf_list), max(maxf_list), max(sum_list))

    # sm_list.sort()
    # wfm_list.sort()
    # mae_list.sort(reverse=True)
    # adpe_list.sort()
    # avge_list.sort()
    # maxe_list.sort()
    # adpf_list.sort()
    # avgf_list.sort()
    # maxf_list.sort()
    # sum_list.sort()

    # print('\n', sm_list[-1], wfm_list[-1], mae_list[-1], adpe_list[-1], avge_list[-1], maxe_list[-1], adpf_list[-1], avgf_list[-1], maxf_list[-1])
    # print('\n', sm_list[-2], wfm_list[-2], mae_list[-2], adpe_list[-2], avge_list[-2], maxe_list[-2], adpf_list[-2], avgf_list[-2], maxf_list[-2])
    # print('\n', sm_list[-3], wfm_list[-3], mae_list[-3], adpe_list[-3], avge_list[-3], maxe_list[-3], adpf_list[-3], avgf_list[-3], maxf_list[-3])
