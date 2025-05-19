# Usar Git LFS (Large File Storage)

## Instalar Git LFS
````
git lfs install
````

## Rastrear arquivos grandes
````
git lfs track "*.pth"
git lfs track "*.zip"
````

## Adicionar e commitar
````
git add .gitattributes
git add model.pth
git commit -m "Add model with Git LFS"
git push origin main
````