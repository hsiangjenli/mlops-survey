from torch import nn
import torch

class SafeModel(nn.Module):

    def __init__(self):
        super(SafeModel, self).__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)
    
if __name__ == "__main__":
    model = SafeModel()

    # save the model
    torch.save(model.state_dict(), "safe_model.pth")