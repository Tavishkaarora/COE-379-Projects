import torch

def est_profitability(model_est, p0, pn, threshold):
  model.eval()
  with torch.no_grad():
