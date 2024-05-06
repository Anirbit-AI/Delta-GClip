UPDATE [12:30pm, 6th May] : Do NOT use this code. Some critical changes are being made. 

Example:
        >>> from Delta-GClip import * <br/>
        >>> optimizer = deltaGClip(model.parameters(), lr=0.5, delta=1e-03, gamma=1) <br/>
        >>> optimizer.zero_grad() <br/>
        >>> loss_fn(model(input), target).backward() <br/>
        >>> optimizer.step()<br/>

In the following link one can see a demonstration code with transformers, <br/>
https://drive.google.com/file/d/1lkEgUJewOTpIpDoweyK985nXC5-RjkJ3/view?usp=sharing
