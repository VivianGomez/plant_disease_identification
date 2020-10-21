# t3_segmentation


### How to run?
## Local environment
Open a command prompt at the root folder of this repository, inside run the following commands:
```
1. pip install virtualenv
2. virtualenv venvpd
3. source venvpd/Scripts/activate
4. pip install -r requirements.txt
5. pip install ipykernel
6. python -m ipykernel install --user --name=venvpd
7. jupyter notebook

```

## Google Colab
```
!shred -u setup_colab.py
!wget "https://raw.githubusercontent.com/VivianGomez/t3_segmentation/master/setup_colab.py" -O setup_colab.py
import setup_colab as setup
setup.setup_workshop()
```
