import os
import modal

LOCAL=False

if LOCAL == False:
   stub = modal.Stub("iris_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("id2223"))
   def f():
       g()


def generate_wine(quality, types, fixed_acidity_max, fixed_acidity_min, volatile_acidity_max, volatile_acidity_min,
                  citric_acid_max, citric_acid_min, residual_sugar_max, residual_sugar_min, chlorides_max,
                  chlorides_min, free_sulfur_dioxide_max, free_sulfur_dioxide_min, total_sulfur_dioxide_max,
                  total_sulfur_dioxide_min, density_max, density_min, pH_max, pH_min, sulphates_max, sulphates_min,
                  alcohol_max, alcohol_min):
    """
    Returns a single wine (as in the Wine Quality dataset) as a single row in a DataFrame
    """
    import pandas as pd
    import random
    
    df = pd.DataFrame({"fixed acidity": [random.uniform(fixed_acidity_max, fixed_acidity_min)],
                          "volatile acidity": [random.uniform(volatile_acidity_max, volatile_acidity_min)],
                          "citric acid": [random.uniform(citric_acid_max, citric_acid_min)],
                          "residual sugar": [random.uniform(residual_sugar_max, residual_sugar_min)],
                          "chlorides": [random.uniform(chlorides_max, chlorides_min)],
                          "free sulfur dioxide": [random.uniform(free_sulfur_dioxide_max, free_sulfur_dioxide_min)],
                          "total sulfur dioxide": [random.uniform(total_sulfur_dioxide_max, total_sulfur_dioxide_min)],
                          "density": [random.uniform(density_max, density_min)],
                          "pH": [random.uniform(pH_max, pH_min)],
                          "sulphates": [random.uniform(sulphates_max, sulphates_min)],
                          "alcohol": [random.uniform(alcohol_max, alcohol_min)],
                          "type": [random.choice(types)]
                         })
    df['quality'] = quality
    return df

def get_random_wine():
    """
    Returns a DataFrame containing one random iris flower
    """
    import pandas as pd
    import random
    
    # generate a random number between 0 and 10
    random_quality = random.choice([3,4,5,6,7,8,9])
    # now generate a wine based on the random number
    
    ranges = {'fixed acidity_6': [3.8, 14.3], 'fixed acidity_5': [4.5, 15.9], 'fixed acidity_7': [4.2, 15.6], 'fixed acidity_8': [3.9, 12.6], 'fixed acidity_4': [4.6, 12.5], 'fixed acidity_3': [4.2, 11.8], 'fixed acidity_9': [6.6, 9.1], 'volatile acidity_6': [0.08, 1.04], 'volatile acidity_5': [0.1, 1.33], 'volatile acidity_7': [0.08, 0.915], 'volatile acidity_8': [0.12, 0.85], 'volatile acidity_4': [0.11, 1.13], 'volatile acidity_3': [0.17, 1.58], 'volatile acidity_9': [0.24, 0.36], 'citric acid_6': [0.0, 1.66], 'citric acid_5': [0.0, 1.0], 'citric acid_7': [0.0, 0.76], 'citric acid_8': [0.03, 0.74], 'citric acid_4': [0.0, 1.0], 'citric acid_3': [0.0, 0.66], 'citric acid_9': [0.29, 0.49], 'residual sugar_6': [0.7, 65.8], 'residual sugar_5': [0.6, 23.5], 'residual sugar_7': [0.9, 19.25], 'residual sugar_8': [0.8, 14.8], 'residual sugar_4': [0.7, 17.55], 'residual sugar_3': [0.7, 16.2], 'residual sugar_9': [1.6, 10.6], 'chlorides_6': [0.015, 0.415], 'chlorides_5': [0.009, 0.611], 'chlorides_7': [0.012, 0.358], 'chlorides_8': [0.014, 0.121], 'chlorides_4': [0.013, 0.61], 'chlorides_3': [0.022, 0.267], 'chlorides_9': [0.018, 0.035], 'free sulfur dioxide_6': [1.0, 112.0], 'free sulfur dioxide_5': [2.0, 131.0], 'free sulfur dioxide_7': [3.0, 108.0], 'free sulfur dioxide_8': [3.0, 105.0], 'free sulfur dioxide_4': [3.0, 138.5], 'free sulfur dioxide_3': [3.0, 289.0], 'free sulfur dioxide_9': [24.0, 57.0], 'total sulfur dioxide_6': [6.0, 294.0], 'total sulfur dioxide_5': [6.0, 344.0], 'total sulfur dioxide_7': [7.0, 289.0], 'total sulfur dioxide_8': [12.0, 212.5], 'total sulfur dioxide_4': [7.0, 272.0], 'total sulfur dioxide_3': [9.0, 440.0], 'total sulfur dioxide_9': [85.0, 139.0], 'density_6': [0.98758, 1.03898], 'density_5': [0.98722, 1.00315], 'density_7': [0.98711, 1.0032], 'density_8': [0.98713, 1.0006], 'density_4': [0.9892, 1.001], 'density_3': [0.9911, 1.0008], 'density_9': [0.98965, 0.997], 'pH_6': [2.72, 4.01], 'pH_5': [2.79, 3.79], 'pH_7': [2.84, 3.82], 'pH_8': [2.88, 3.72], 'pH_4': [2.74, 3.9], 'pH_3': [2.87, 3.63], 'pH_9': [3.2, 3.41], 'sulphates_6': [0.23, 1.95], 'sulphates_5': [0.27, 1.98], 'sulphates_7': [0.22, 1.36], 'sulphates_8': [0.25, 1.1], 'sulphates_4': [0.25, 2.0], 'sulphates_3': [0.28, 0.86], 'sulphates_9': [0.36, 0.61], 'alcohol_6': [8.4, 14.0], 'alcohol_5': [8.0, 14.9], 'alcohol_7': [8.6, 14.2], 'alcohol_8': [8.5, 14.0], 'alcohol_4': [8.4, 13.5], 'alcohol_3': [8.0, 12.6], 'alcohol_9': [10.4, 12.9]}
    
    wine_df = generate_wine(random_quality, ['white', 'red'], ranges[f'fixed acidity_{random_quality}'][0], ranges[f'fixed acidity_{random_quality}'][1], ranges[f'volatile acidity_{random_quality}'][0], ranges[f'volatile acidity_{random_quality}'][1], ranges[f'citric acid_{random_quality}'][0], ranges[f'citric acid_{random_quality}'][1], ranges[f'residual sugar_{random_quality}'][0], ranges[f'residual sugar_{random_quality}'][1], ranges[f'chlorides_{random_quality}'][0], ranges[f'chlorides_{random_quality}'][1], ranges[f'free sulfur dioxide_{random_quality}'][0], ranges[f'free sulfur dioxide_{random_quality}'][1], ranges[f'total sulfur dioxide_{random_quality}'][0], ranges[f'total sulfur dioxide_{random_quality}'][1], ranges[f'density_{random_quality}'][0], ranges[f'density_{random_quality}'][1], ranges[f'pH_{random_quality}'][0], ranges[f'pH_{random_quality}'][1], ranges[f'sulphates_{random_quality}'][0], ranges[f'sulphates_{random_quality}'][1], ranges[f'alcohol_{random_quality}'][0], ranges[f'alcohol_{random_quality}'][1])
        
    return wine_df

def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    iris_df = get_random_wine()

    iris_fg = fs.get_feature_group(name="iris",version=1)
    iris_fg.insert(iris_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        stub.deploy("iris_daily")
        with stub.run():
            f()
