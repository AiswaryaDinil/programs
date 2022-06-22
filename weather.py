weather=[{"district": "pkd", "temp":30},
        {"district": "tvm", "temp":29},
        {"district": "pkd", "temp":32},
        {"district": "tcr", "temp":24},
        {"district": "tcr", "temp":28},
        {"district": "mpm", "temp":30},
        {"district": "idk", "temp":26}]

out={}
for data in weather:
    dist_name=data["district"]
    cur_temp=data["temp"]
    if dist_name in out:
        old_temp=out[dist_name]
        if cur_temp >old_temp:
            out[dist_name]=cur_temp
    else:
        out[dist_name]=cur_temp
print(out)

sort_ord=sorted(out.items(),key=lambda item:item[1] )
print(sort_ord)