from torch.optim.optimizer import Optimizer, required
import copy

class Delta-GClip(Optimizer):
   def __init__(self, params, lr=required, delta=required, gamma=required, weight_decay):
        defaults = dict(weight_decay=weight_decay)
        super(Delta-GClip, self).__init__(params, defaults)


   def step(self,closure=None):
	norm_grad_f = torch.nn.utils.clip_grad_norm_(net.parameters(), max_norm=float("inf")).item()
        h = min(eta, eta * max(delta, gamma / norm_grad_f) )
        for g in optimizer.param_groups:
        	g["lr"] = h
  
