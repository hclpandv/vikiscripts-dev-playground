declare -a a=(sp-aks-element-01
sp-aks-element-02
sp-aks-element-03        
sp-aks-element-04
)

for i in "${a[@]}"
do
    echo "sp $i"
done