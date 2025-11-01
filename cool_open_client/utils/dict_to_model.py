from __future__ import annotations

from typing import Any, Dict, Type, TypeVar


T = TypeVar("T")


def dict_to_model(model: Type[T], dictionary: Dict[str, Any]) -> T:
    """
    Converts a dictionary to an OpenAPI model.

    Args:
        model (Type[T]): The model class to instantiate.
        dictionary (dict): A dictionary to convert.

    Returns:
        T: The instantiated model.
    """
    if dictionary is None:
        raise TypeError("dictionary cannot be None")

    if isinstance(dictionary, model):
        return dictionary

    if hasattr(model, "model_validate"):
        payload = dictionary

        if (
            getattr(model, "__name__", None) == "UnitResponseData"
            and isinstance(dictionary, dict)
        ):
            ambient_value = dictionary.get("ambientTemperature")
            if isinstance(ambient_value, float):
                # Round half-degree readings so the StrictInt schema accepts the value.
                payload = {**dictionary}
                payload["ambientTemperature"] = int(round(ambient_value))

        return model.model_validate(payload)

    if hasattr(model, "from_dict"):
        return model.from_dict(dictionary)

    if isinstance(dictionary, dict):
        attribute_map: Dict[str, str] = getattr(model, "attribute_map", {})
        inverse_map = {value: key for key, value in attribute_map.items()}
        payload = {
            inverse_map.get(key, key): value for key, value in dictionary.items()
        }
        return model(**payload)

    raise TypeError(f"Unsupported payload type {type(dictionary)!r} for model {model!r}")
