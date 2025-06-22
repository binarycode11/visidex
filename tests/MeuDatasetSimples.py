import os
import torch
import requests
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
from PIL import Image

class MeuDatasetSimples(Dataset):
    def __init__(self, root, train=True, transform=None, download=False):
        self.root = root
        self.train = train
        self.transform = transform
        self.url_base = 'https://raw.githubusercontent.com/usuario/repositorio/main/'  # Substitua aqui
        self.train_file = 'train.pt'
        self.test_file = 'test.pt'

        if download:
            self._download()

        file = self.train_file if train else self.test_file
        path = os.path.join(self.root, file)
        self.data, self.targets = torch.load(path)

    def __getitem__(self, idx):
        img = self.data[idx].numpy()
        img = Image.fromarray(img, mode='L')
        if self.transform:
            img = self.transform(img)
        return img, int(self.targets[idx])

    def __len__(self):
        return len(self.data)

    def _download(self):
        os.makedirs(self.root, exist_ok=True)
        for fname in [self.train_file, self.test_file]:
            url = self.url_base + fname
            path = os.path.join(self.root, fname)
            if not os.path.exists(path):
                print(f"Baixando {fname}...")
                r = requests.get(url)
                with open(path, 'wb') as f:
                    f.write(r.content)
            else:
                print(f"{fname} já existe. Ignorando download.")

# -----------------------
# 🧪 Exemplo de uso (main)
# -----------------------
if __name__ == '__main__':
    root = './meudata'
    train_file = os.path.join(root, 'train.pt')
    test_file = os.path.join(root, 'test.pt')

    # ✅ Verifica se os arquivos já existem antes de instanciar o dataset com download
    arquivos_existem = os.path.exists(train_file) and os.path.exists(test_file)

    dataset = MeuDatasetSimples(
        root=root,
        train=True,
        transform=ToTensor(),
        download=not arquivos_existem  # Só baixa se não tiver os arquivos
    )

    print("Dataset carregado com", len(dataset), "amostras.")
    img, label = dataset[0]
    print("Shape:", img.shape, "| Label:", label)
