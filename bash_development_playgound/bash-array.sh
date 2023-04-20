declare -a a=(sp-hk01-eas-u-future-setk-svoc01
sp-hk01-eas-u-future-setk-svoa01
sp-aks-hk01-eas-u-setk-kv01
sp-aks-hk01-eas-u-future-setk-blob01        
sp-hk01-eas-p-future-setk-svoc01
sp-hk01-eas-p-future-setk-svoa01
sp-hk01-eas-p-setk-adbdevops01
sp-aks-hk01-eas-p-future-setk-db01
sp-aks-hk01-eas-p-setk-kv01
sp-aks-hk01-eas-p-future-setk-blob01
sp-hk01-eas-p-setk-autosys01
sp-hk01-eas-p-dna-setk01

)

for i in "${a[@]}"
do
    echo "sp $i"
done