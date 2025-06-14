import torch

safe_model_path = "safe_model.pth"
malicious_model_path = "malicious_model.pth"

s_model = torch.load(safe_model_path)
m_model = torch.load(malicious_model_path, weights_only=False)
