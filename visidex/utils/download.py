import torch

def load_model(model_class, weights_url, pretrained=True, map_location="cpu"):
    """
    Loads a PyTorch model from a URL.

    Args:
        model_class: The class of the model to load.
        weights_url: The URL of the model weights.
        pretrained: Whether to load pretrained weights. Defaults to True.
        map_location: Device to map model parameters to. Defaults to "cpu".

    Returns:
        The loaded model.
    """
    model = model_class()
    if pretrained:
        try:
            state_dict = torch.hub.load_state_dict_from_url(
                weights_url,
                map_location=map_location,
                progress=True,
                check_hash=True,
            )
            model.load_state_dict(state_dict)
        except Exception as e:
            print(f"Error loading pretrained weights: {e}")
            return model # Return the model even if loading fails
    model.eval()
    return model

