from torch.optim.optimizer import Optimizer, required
import copy
import torch

class deltaGClip-c(Optimizer):
    def __init__(self, params, lr=0.1, delta=1e-03, gamma=0.25):
        defaults = dict(lr=lr, delta=delta, gamma=gamma)
        super(deltaGClip, self).__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        """Performs a single optimization step."""
        for group in self.param_groups:
            delta = group['delta']
            gamma = group['gamma']
            lr = group['lr']
            for p in group['params']:
                if p.grad is None:
                    continue
                grad = p.grad.data
                norm = grad.norm()
                if norm != 0 and not torch.isnan(norm):
                    g_norm = min(1, max(delta, gamma / norm))
                    scaled_grad = g_norm * grad
                    p.data -= lr * scaled_grad
  
