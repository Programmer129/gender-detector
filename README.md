# Gender Detector

Gender detector is a AI bases App. The App can recognise human gender

## Usage

Run this command to train AI model.
Make sure --dataset argument was directory name of your data

```
python gender_detect_model.py
--dataset people
--model output/simple_nn.model
--label-bin output/simple_nn_lb.pickle
--plot output/simple_nn_plot.png
```

After training run this commands to test AI model

```
python predict.py
--image images/man.jpg
--model output/simple_nn.model
--label-bin output/simple_nn_lb.pickle
--width 32
--height 32
--flatten 1

python predict.py
--image images/woman.jpg
--model output/smallvggnet.model
--label-bin output/smallvggnet_lb.pickle
--width 64
--height 64
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)