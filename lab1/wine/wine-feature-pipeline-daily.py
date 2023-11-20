import os
import hopsworks
import pandas as pd
import random

# import modal

# LOCAL = True

# if LOCAL == False:
#     stub = modal.Stub("wine_daily")
#     image = modal.Image.debian_slim().pip_install(["hopsworks"])

#     @stub.function(
#         image=image,
#         schedule=modal.Period(days=1),
#         secret=modal.Secret.from_name("HOPSWORKS_API_KEY"),
#     )
#     def f():
#         g()


def generate_wine(
    quality,
    # types,
    # fixed_acidity_max,
    # fixed_acidity_min,
    volatile_acidity_max,
    volatile_acidity_min,
    citric_acid_max,
    citric_acid_min,
    # residual_sugar_max,
    # residual_sugar_min,
    chlorides_max,
    chlorides_min,
    # free_sulfur_dioxide_max,
    # free_sulfur_dioxide_min,
    total_sulfur_dioxide_max,
    total_sulfur_dioxide_min,
    density_max,
    density_min,
    # pH_max,
    # pH_min,
    # sulphates_max,
    # sulphates_min,
    alcohol_max,
    alcohol_min,
):
    """
    Returns a single wine (as in the Wine Quality dataset) as a single row in a DataFrame
    """

    df = pd.DataFrame(
        {
            # "type": [random.choice(types)],
            # "fixed acidity": [random.uniform(fixed_acidity_max, fixed_acidity_min)],
            "volatile_acidity": [
                random.uniform(volatile_acidity_max, volatile_acidity_min)
            ],
            "citric_acid": [random.uniform(citric_acid_max, citric_acid_min)],
            # "residual sugar": [random.uniform(residual_sugar_max, residual_sugar_min)],
            "chlorides": [random.uniform(chlorides_max, chlorides_min)],
            # "free sulfur dioxide": [
            #     random.uniform(free_sulfur_dioxide_max, free_sulfur_dioxide_min)
            # ],
            "total_sulfur_dioxide": [
                random.uniform(total_sulfur_dioxide_max, total_sulfur_dioxide_min)
            ],
            "density": [random.uniform(density_max, density_min)],
            # "pH": [random.uniform(pH_max, pH_min)],
            # "sulphates": [random.uniform(sulphates_max, sulphates_min)],
            "alcohol": [random.uniform(alcohol_max, alcohol_min)],
        }
    )
    df["quality"] = quality
    return df


def get_random_wine():
    """
    Returns a DataFrame containing one random iris flower
    """

    # generate a random number between 0 and 10
    random_quality = random.choice([0, 1])
    # now generate a wine based on the random number

    ranges = {
            "type_1": [0, 1],
            "type_0": [0, 1],
            "fixed_acidity_1": [3.8, 15.6],
            "fixed_acidity_0": [4.2, 15.9],
            "volatile_acidity_1": [0.08, 1.04],
            "volatile_acidity_0": [0.1, 1.58],
            "citric_acid_1": [0.0, 1.66],
            "citric_acid_0": [0.0, 1.0],
            "residual_sugar_1": [-0.8125291163148622, 65.8],
            "residual_sugar_0": [0.6, 23.5],
            "chlorides_1": [0.012, 0.415],
            "chlorides_0": [0.009, 0.611],
            "free_sulfur_dioxide_1": [1.0, 112.0],
            "free_sulfur_dioxide_0": [2.0, 289.0],
            "total_sulfur_dioxide_1": [6.0, 294.0],
            "total_sulfur_dioxide_0": [6.0, 440.0],
            "density_1": [0.98711, 1.03898],
            "density_0": [0.98722, 1.00315],
            "pH_1": [2.72, 4.01],
            "pH_0": [2.74, 3.9],
            "sulphates_1": [0.1116379096465947, 1.95],
            "sulphates_0": [0.25, 2.0],
            "alcohol_1": [8.4, 14.2],
            "alcohol_0": [8.0, 14.9],
    }
    

    wine_df = generate_wine(
        random_quality,
        # ranges[f"type_{random_quality}"],
        # ranges[f"fixed acidity_{random_quality}"][0],
        # ranges[f"fixed acidity_{random_quality}"][1],
        ranges[f"volatile_acidity_{random_quality}"][0],
        ranges[f"volatile_acidity_{random_quality}"][1],
        ranges[f"citric_acid_{random_quality}"][0],
        ranges[f"citric_acid_{random_quality}"][1],
        # ranges[f"residual sugar_{random_quality}"][0],
        # ranges[f"residual sugar_{random_quality}"][1],
        ranges[f"chlorides_{random_quality}"][0],
        ranges[f"chlorides_{random_quality}"][1],
        # ranges[f"free sulfur dioxide_{random_quality}"][0],
        # ranges[f"free sulfur dioxide_{random_quality}"][1],
        ranges[f"total_sulfur_dioxide_{random_quality}"][0],
        ranges[f"total_sulfur_dioxide_{random_quality}"][1],
        ranges[f"density_{random_quality}"][0],
        ranges[f"density_{random_quality}"][1],
        # ranges[f"pH_{random_quality}"][0],
        # ranges[f"pH_{random_quality}"][1],
        # ranges[f"sulphates_{random_quality}"][0],
        # ranges[f"sulphates_{random_quality}"][1],
        ranges[f"alcohol_{random_quality}"][0],
        ranges[f"alcohol_{random_quality}"][1],
    )

    return wine_df


def g():


    project = hopsworks.login()
    fs = project.get_feature_store()

    iris_df = get_random_wine()

    iris_fg = fs.get_feature_group(name="wine_final", version=1)
    iris_fg.insert(iris_df)


if __name__ == "__main__":
    g()
    # else:
    #     stub.deploy("wine_daily")
    #     with stub.run():
    #         f()
