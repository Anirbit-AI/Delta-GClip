>>> **In the code Delta-GClip-c we give a package implementation of a *variant* of the delta-GClip optimizer get - which was recently shown to be a (possibly the only) step-length scheduling algorithm that provably converges on deep neural net losses, https://arxiv.org/abs/2404.08624. In this -c variant **

Example:
        >>> from Delta-GClip import * <br/>
        >>> optimizer = deltaGClip(model.parameters(), lr=0.5, delta=1e-03, gamma=1) <br/>
        >>> optimizer.zero_grad() <br/>
        >>> loss_fn(model(input), target).backward() <br/>
        >>> optimizer.step()<br/>

In the following link one can see a demonstration code with transformers, <br/>
https://drive.google.com/file/d/1lkEgUJewOTpIpDoweyK985nXC5-RjkJ3/view?usp=sharing
