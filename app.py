<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paracetamol Dosage Calculator</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f4f7f6; color: #333; }
        .container { max-width: 500px; background: #fff; margin: 30px auto; padding: 25px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { font-family: "Georgia", serif; font-size: 26px; color: #2c3e50; margin-top: 0; }
        p { color: #666; font-size: 15px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; font-weight: bold; font-size: 14px; }
        input, select { width: 100%; padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; font-size: 16px; background-color: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; transition: background 0.2s; }
        button:hover { background-color: #219653; }
        .result { margin-top: 20px; padding: 15px; border-radius: 4px; display: none; font-size: 16px; line-height: 1.5; }
        .disclaimer { margin-top: 25px; font-size: 12px; color: #7f8c8d; border-top: 1px solid #eee; padding-top: 15px; text-align: justify; }
    </style>
</head>
<body>

<div class="container">
    <h1>Paracetamol Dosage Calculator</h1>
    <p>Calculate the appropriate dose based on child's weight.</p>

    <div class="form-group">
        <label for="weight">Child's Weight (kg):</label>
        <input type="number" id="weight" placeholder="e.g. 10" min="0.5" max="60" step="0.1">
    </div>

    <div class="form-group">
        <label for="concentration">Concentration:</label>
        <select id="concentration">
            <option value="120-5">120 mg / 5 ml</option>
            <option value="250-5">250 mg / 5 ml</option>
        </select>
    </div>

    <button onclick="calculateDose()">Calculate</button>

    <div id="output" class="result"></div>

    <div class="disclaimer">
        <strong>Medical Disclaimer:</strong> This calculator provides an estimation based on standard pediatric dosage guidelines (15 mg/kg per dose). It is for educational/reference purposes only. Always consult a pediatrician or pharmacist before administering medication. Do not exceed 4 doses in 24 hours.
    </div>
</div>

<script>
    function calculateDose() {
        const weightInput = document.getElementById('weight').value;
        const weight = parseFloat(weightInput);
        const concentrationValue = document.getElementById('concentration').value;
        const outputDiv = document.getElementById('output');

        if (!weightInput || isNaN(weight) || weight < 0.5 || weight > 60) {
            outputDiv.style.display = 'block';
            outputDiv.style.backgroundColor = '#f8d7da';
            outputDiv.style.color = '#721c24';
            outputDiv.innerHTML = '<strong>Error:</strong> Please enter a valid weight between 0.5 and 60 kg.';
            return;
        }

        let requiredMg = weight * 15;

        if (requiredMg > 1000) {
            requiredMg = 1000; 
        }

        const [mgPerUnit, mlPerUnit] = concentrationValue.split('-').map(Number);
        const requiredMl = (requiredMg * mlPerUnit) / mgPerUnit;

        outputDiv.style.display = 'block';
        outputDiv.style.backgroundColor = '#d4edda';
        outputDiv.style.color = '#155724';
        outputDiv.innerHTML = `
            <strong>Results:</strong><br>
            • Required Dose: <strong>${requiredMg.toFixed(1)} mg</strong><br>
            • Liquid Amount: <strong>${requiredMl.toFixed(1)} ml</strong>
        `;
    }
</script>

</body>
</html>
