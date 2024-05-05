Example:
        >>> from Delta-GClip import *
        >>> optimizer = deltaGClip(model.parameters(), lr=0.1, delta=1e-02, gamma-0.25)
        >>> optimizer.zero_grad()
        >>> loss_fn(model(input), target).backward()
        >>> optimizer.step()
