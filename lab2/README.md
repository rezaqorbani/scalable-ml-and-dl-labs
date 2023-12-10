# LAB 2 Fine-tuning Whisper model on Swedish audio dataset

Whisper is a state-of-the-art automatic speech recognition(ASR) model created by OpenAI. It is able to translate and transcribe multiple different languages. In this project the "small" Whisper model with 244M parameters was used. The dataset that wasa used for fine-tuning the Whisper model was the Swedish subset of the Mozilla foundation common voice 11 dataset.  

Each audio in the dataset will be truncated or padded to 30 second snippets and then converted to the log-Mel spectrogram. Once they are in the form of log-Mel spectrograms they will be sent into the Whisper model architecture. Training was done on Google Colab and during the training checkpoints were saved to google drive in case of disconnections. Additionally the models were also pushed to a huggingface model repo along with the tensorboard data to visualize the metrics.

We started by training the model with smaller number of steps and learning rate in order to get a baseline. Then we increased these parameters to see how the model would perform. As we anticipated, we traded longer training time for better performance. Howerver, we had issues with the trainig where we would get unexpected results and disconnection, especially during the training with higher number of steps.

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

The model can be found at: '[HuggingFace Model Repo](https://huggingface.co/Yulle/WhisperCheckpoints3/tree/main)'

The visualization of metrics during model training can be found at:'[HuggingFace Model tensorboard](https://huggingface.co/Yulle/WhisperCheckpoints3/tensorboard)'

## Huggingface App

We created an app hosted on Huggingface spaces using our fine tuned Whisper model. The app allows searching for youtube videos using voice search in Swedish by letting the user speak into their microphone. The top video will be fetched and the audio of the video will also be transcribed into Swedish text. The app also allows: transcription of the input from the user microphone, transcription of user uploaded audio file, and transcription of Youtube videos using URL links as an input. 

The app can be found here: '[HuggingFace App](https://huggingface.co/spaces/rezaqorbani/whisper-transcribe-swedish)'

## Model centric approach to improve model

* There are different ways to improve the Whisper model from a model-centric viewpoint. The first thing we did was hyperparameter tuning. We tried many different parameters and trained to 1000 steps to how the WER was affected. We tried changing the: learning rate, batch size, gradient accumulation, eval steps, warmup steps etc. The best parameters were shown above.

* Another way to improve the Whisper model would be to use a larger pretrained Whisper model. The larger models have better performance than the smaller ones, however, due to limited memory on google colab instances we were not able to run larger pretrained Whisper models.

## Data centric approach to improve model

* A bigger dataset would be beneficial for training the Whisper model
* Data augmentation such as adding noise or varying speed, pitch etc. would improve the model. We discovered that it is not always able to distinguish the word being spoken if there is background noise
