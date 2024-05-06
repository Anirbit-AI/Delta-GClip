> In the code deltaGClip_c we give a package implementation of a *variant* of the delta-GClip optimizer get - which was recently shown to be a (possibly the only) step-length scheduling algorithm that provably converges on deep neural net losses, https://arxiv.org/abs/2404.08624. In this -c variant the norm of the gradient of the loss (based on which the modified clipping is done) is replaced by the norm of the partial derivative of the loss w.r.t the parameter being updated - thus effectively now we have different adaptive learning rates for each parameter of the model. * In the following link one can see a demonstration of deltaGclip_c with transformers,
https://drive.google.com/file/d/1lkEgUJewOTpIpDoweyK985nXC5-RjkJ3/view?usp=sharing. Thanks to Chong Zhe Kang @UManchester for helping with this variant.

Example: <br/>
                >>> from Delta-GClip import * <br/>
                >>> optimizer = deltaGClip_c(model.parameters(), lr=0.5, delta=1e-03, gamma=1) <br/>
                >>> optimizer.zero_grad() <br/>
                >>> loss_fn(model(input), target).backward() <br/>
                >>> optimizer.step()<br/>

       


