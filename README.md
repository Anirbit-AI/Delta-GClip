> In the code deltaGClip_c we give a package implementation of a *variant* of the delta-GClip optimizer - which was recently shown to be a (possibly the only) step-length scheduling algorithm that provably converges on deep neural net losses, https://arxiv.org/abs/2404.08624. In this _c variant, the norm of the gradient of the loss (based on which the modified clipping is done) is replaced by the norm of the partial derivative of the loss w.r.t the parameter being updated - thus effectively now we have different adaptive learning rates for each parameter of the model. In the following link, we have also uploaded a demonstration of deltaGclip_c with transformers, https://github.com/procheta/Delta-GClip/blob/main/deltaGClip_c_vs_Other_Optimisers_on_Transformers.ipynb. <br/>
>
> Thanks to Chong Zhe Kang @UManchester for helping with this variant.

Example: <br/>
                >>> from Delta-GClip import * <br/>
                >>> optimizer = deltaGClip_c(model.parameters(), lr=0.5, delta=1e-03, gamma=1) <br/>
                >>> optimizer.zero_grad() <br/>
                >>> loss_fn(model(input), target).backward() <br/>
                >>> optimizer.step()<br/>






<!-- readme: collaborators,contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/procheta">
                    <img src="https://avatars.githubusercontent.com/u/16814552?v=4" width="100;" alt="procheta"/>
                    <br />
                    <sub><b>PROCHETA SEN</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/matteo-tucat">
                    <img src="https://avatars.githubusercontent.com/u/56000401?v=4" width="100;" alt="matteo-tucat"/>
                    <br />
                    <sub><b>matteo-tucat</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/akhilendra1811">
                    <img src="https://avatars.githubusercontent.com/u/96082666?v=4" width="100;" alt="akhilendra1811"/>
                    <br />
                    <sub><b>Akhilendra Sabherwal</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/Anirbit-AI">
                    <img src="https://avatars.githubusercontent.com/u/106439647?v=4" width="100;" alt="Anirbit-AI"/>
                    <br />
                    <sub><b>Anirbit </b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: collaborators,contributors -end -->

       


