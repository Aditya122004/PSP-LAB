attendance={"Python":[(1,["P","A","P","P","A"]),(2,["P","P","P","P","A"]),(3,["A","A","P","P","P"])],
            "DSA":[(1,["P","A","P","P","A"]),(2,["A","P","A","P","P"]),(3,["P","P","A","P","A"])]}
for subject,records in attendance.items():
    print(f"Subject:{subject}")
    for roll_N,days in records:
        total_days=len(days)
        pre_days=days.count("P")
        ab_days=days.count("A")
        percentage=(pre_days/total_days)*100
        print(f"Roll No:{roll_N}")
        print(f"Total Days:{total_days}")
        print(f"present={pre_days},absent={ab_days}")
        print(f"Att. Percentage={percentage:.2f}")
