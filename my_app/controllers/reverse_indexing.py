def reverse_indexing(dictionary):
        newList = []
        rev = {}
        skill_name = ""
        slo = ""
        unit_name = ""
        for k,v  in dictionary.items():
            if v.equals("unit_name"):
                unit_name = v
            if v.equals("skills"):
                for k1,v1 in v.items():
                    if v1.equals("skill_name"):
                        skill_name = v1
                    if v1.equals("skill_sos"):
                        slo = v1
                    rev.update({"skill_slos":
                                    [{
                                        "unit_name":unit_name,
                                        "skill_name": skill_name,
                                        "skill_slo": slo
                                    }]})
            newList.append(rev)

        return newList

