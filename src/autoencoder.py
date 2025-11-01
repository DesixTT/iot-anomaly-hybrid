
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Dropout, GaussianNoise
from tensorflow.keras.models import Model

def build_denoising_autoencoder(input_dim, encoding_dim=8, noise_factor=0.1):
    input_layer = Input(shape=(input_dim,))
    noisy_input = GaussianNoise(noise_factor)(input_layer)

    # Encoder
    x = Dense(64, activation='relu')(noisy_input)
    x = BatchNormalization()(x)
    x = Dropout(0.1)(x)
    x = Dense(32, activation='relu')(x)
    x = BatchNormalization()(x)
    encoded = Dense(encoding_dim, activation='relu')(x)

    # Decoder
    x = Dense(32, activation='relu')(encoded)
    x = BatchNormalization()(x)
    x = Dense(64, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.1)(x)
    decoded = Dense(input_dim, activation='sigmoid')(x)

    autoencoder = Model(input_layer, decoded)
    encoder = Model(input_layer, encoded)
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder, encoder
