from keras_core.api_export import keras_core_export
from keras_core.optimizers.adam import Adam
from keras_core.optimizers.optimizer import Optimizer
from keras_core.optimizers.sgd import SGD
from keras_core.saving import serialization_lib

ALL_OBJECTS = {
    Optimizer,
    Adam,
    SGD,
}
ALL_OBJECTS_DICT = {cls.__name__.lower(): cls for cls in ALL_OBJECTS}


@keras_core_export("keras_core.optimizers.serialize")
def serialize(optimizer):
    """Returns the optimizer configuration as a Python dict.

    Args:
        optimizer: An `Optimizer` instance to serialize.

    Returns:
        Python dict which contains the configuration of the optimizer.
    """
    return serialization_lib.serialize_keras_object(optimizer)


@keras_core_export("keras_core.optimizers.deserialize")
def deserialize(config, custom_objects=None):
    """Returns a Keras optimizer object via its configuration.

    Args:
        config: Optimizer configuration dictionary.
        custom_objects: Optional dictionary mapping names (strings) to custom
            objects (classes and functions) to be considered during
            deserialization.

    Returns:
        A Keras Optimizer instance.
    """
    # Make deserialization case-insensitive for built-in optimizers.
    if config["class_name"].lower() in ALL_OBJECTS_DICT:
        config["class_name"] = config["class_name"].lower()

    print("deserialize:", config)
    return serialization_lib.deserialize_keras_object(
        config,
        module_objects=ALL_OBJECTS_DICT,
        custom_objects=custom_objects,
    )


@keras_core_export("keras_core.optimizers.get")
def get(identifier):
    """Retrieves a Keras Optimizer instance.

    Args:
        identifier: Optimizer identifier, one of:
            - String: name of an optimizer
            - Dictionary: configuration dictionary.
            - Keras Optimizer instance (it will be returned unchanged).

    Returns:
        A Keras Optimizer instance.
    """
    print("call get with", identifier)
    if isinstance(identifier, Optimizer):
        return identifier
    elif isinstance(identifier, dict):
        return deserialize(identifier)
    elif isinstance(identifier, str):
        config = {"class_name": identifier, "config": {}}
        opt = deserialize(config)
        print(opt)
        return opt
    else:
        raise ValueError(
            f"Could not interpret optimizer identifier: {identifier}"
        )
