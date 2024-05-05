Example:
        >>> from Delta-GClip import * <br/>
        >>> optimizer = deltaGClip(model.parameters(), lr=0.1, delta=1e-02, gamma-0.25) <br/>
        >>> optimizer.zero_grad() <br/>
        >>> loss_fn(model(input), target).backward() <br/>
        >>> optimizer.step()<br/>
