from torch.optim.optimizer import Optimizer, required
import copy

class Delta-GClip(Optimizer):
    def __init__(self, params, lr=0.1, delta=1e-03, gamma=0.25):
        defaults = dict(lr=lr, delta=delta, gamma=gamma)
        super(deltaGClipOptimizer, self).__init__(params, defaults)

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
   def step(self,closure=None):
	norm_grad_f = torch.nn.utils.clip_grad_norm_(net.parameters(), max_norm=float("inf")).item()
        h = min(eta, eta * max(delta, gamma / norm_grad_f) )
        for g in optimizer.param_groups:
        	g["lr"] = h
  
