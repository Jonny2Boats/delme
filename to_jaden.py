
def to_jaden_case(string):
    # Step through string, when space next char tocaps
    jadenString=""
    capsBool= True

    for i in string:
        if capsBool==True:
            i= i.upper()
            capsBool=False  
        elif capsBool==False:
            i= i.lower()
        if i == " ":
            capsBool=True
        jadenString+=i
    return jadenString

print(to_jaden_case("GHylvBXq UCMItJTFI WMNFDby WPTv IWxiecg CodayEWZ CLox ZX FbwVLogfgt ILuPjO K NxCd Zp NiuAIL GeIZ G AZwGb NAfPuxQn XIR JNSCDtrE NO ENwH P WI Ox LlyRUJ EM Xwb"))