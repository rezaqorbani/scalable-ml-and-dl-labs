# LAB 2 Fine-tuning Whisper model on Swedish audio dataset

Whisper is a state-of-the-art automatic speech recognition(ASR) model created by OpenAI. It is able to translate and transcribe multiple different languages. In this project the "small" Whisper model with 244M parameters was used. The dataset that wasa used for fine-tuning the Whisper model was the Swedish subset of the [Mozilla foundation common voice 11](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) dataset.  

Each audio in the dataset will be truncated or padded to 30 second snippets and then converted to the log-Mel spectrogram. Once they are in the form of log-Mel spectrograms they will be sent into the Whisper model architecture. Training was done on Google Colab and during the training checkpoints were saved to google drive in case of disconnections. Additionally the models were also pushed to a huggingface model repo along with the tensorboard data to visualize the metrics.

We started by training the model with smaller number of steps and high learning rate in order to get a baseline. Then we increased the number of steps and decreased the learning, expecting higher performance. As expected, we traded longer training time for better performance. Howerver, we had some issues with the trainig in the beginning where we would get unexpected results and disconnection, especially during the training with higher number of steps. We expect that if we had access to our own GPU, we would have direct control over the hardware which means we could debug the issues more easily and let training run for longer time without interruptions.

## Training Hyperparameters

### Hyperparameters of base model

| **Hyperparameter** | **Value** |
|--------------------|-----------|
| `num_train_epochs` | 1         |
| `per_device_train_batch_size` | 16 |
| `gradient_accumulation_steps` | 1  |
| `learning_rate` | 1e-4  |
| `warmup_steps` | 50  |
| `max_steps` | 1000  |
| `gradient_checkpointing` | True  |
| `fp16` | True  |
| `per_device_eval_batch_size` | 8  |
| `generation_max_length` | 225  |
| `save_steps` | 250  |
| `eval_steps` | 250  |

### Hyperparameters of best model

| **Hyperparameter** | **Value** |
|--------------------|-----------|
| `num_train_epochs` | 1         |
| `per_device_train_batch_size` | 16 |
| `gradient_accumulation_steps` | 1  |
| `learning_rate` | 1e-5  |
| `warmup_steps` | 500  |
| `max_steps` | 4000  |
| `gradient_checkpointing` | True  |
| `fp16` | True  |
| `per_device_eval_batch_size` | 8  |
| `generation_max_length` | 225  |
| `save_steps` | 500  |
| `eval_steps` | 500  |

## Results

### Results of base model

The base model had the following word error rate during training:
| **Step** | **WER** |
|----------|---------|
| 250      | 43.05   |
| 500      | 35.22   |
| 750      | 29.62   |
| 1000     | 26.68   |

### Results of best model

The best model had the following word error rate during training:
| **Step** | **WER** |
|----------|---------|
| 500      | 68.59   |
| 1000     | 21.8    |
| 1500     | 21.13   |
| 2000     | 20.62   |
| 2500     | 20.14   |
| 3000     | 19.93   |

The best model can be found at: [Model card of best model](https://huggingface.co/Yulle/WhisperCheckpoints3) and the visualization of metrics during model training can be found at: [Tensorboard for best model](https://huggingface.co/Yulle/WhisperCheckpoints3/tensorboard)

Similarly, the base model can be found: [Model card of base model](https://huggingface.co/rezaqorbani/WhisperCheckpoints) and the tensorboard data for base model can be found: [Tensorboard for base model](https://huggingface.co/rezaqorbani/WhisperCheckpoints/tensorboard)

## Huggingface App

We created an app hosted on Huggingface spaces using our fine tuned Whisper model. The app allows searching for youtube videos using voice search in Swedish by letting the user speak into their microphone. The top video will be fetched and the audio of the video will also be transcribed into Swedish text. The app also allows: transcription of the input from the user microphone, transcription of user uploaded audio file, and transcription of Youtube videos using URL links as an input.

The app can be found here: [HuggingFace App](https://huggingface.co/spaces/rezaqorbani/whisper-transcribe-swedish)

## Model centric approach to improve model

* There are different ways to improve the Whisper model from a model-centric viewpoint. The technique that we used was hyperparameter tuning. We first trained to 1000 steps to see how the WER was affected and to get a good ballpark quickly to begin with and know how to change the hyperparameters. We then changed the following hyperparameters: learning rate, batch size, gradient accumulation, eval/train steps, warmup steps. What we realized was that changing the number steps, and learning rate had the biggest effect, but also changing the warmup step (related to the ADAM optimizer) had also an effect. The best hyperparameters we achieved can be seen above. One thing that we did not try was to run the model with full precision instead of half precision. This would have been interesting to see if it would have had an effect on the WER. We expect that larger number of steps will result in minimal improvements in WER, but will take longer time to train. We also expect that the learning rate will have a similar effect, where a lower learning rate will result in minimal improvements in WER, but will take longer time to train.
* Another way to improve the Whisper model would be to use a larger pretrained Whisper model. The larger models have better performance than the smaller ones, however, due to limited memory on google colab instances we were not able to run larger pretrained Whisper models.

## Data centric approach to improve model

* Using more data, for example by using additional data, would directly result in higher performance. One such datasets are [NST Swedish ASR Database](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-56/) which includes 124 GB of Swedish speech data. Some preprocessing would potentially be required to convert the data into the format that Whisper model expects. In order to increase the robustness of the model when it comes to dialects, we could use another dataset, called [SweDia 2000](https://snd.gu.se/en/catalogue/dataset/ext0020-1) which contains recordings of a little more than 1300 speakers representing 107 Swedish dialects.
* Data augmentation such as adding noise or varying speed, pitch etc. would improve the model. While testing the model, we discovered that the Whisper model is not always able to distinguish the word being spoken if there is background noise
