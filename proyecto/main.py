from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


empresa = {
    'mision': 'Brindar productos de salud',
    'vision': 'Ser la farmacia líder en el país',
    'direccion': 'Av. Siempre Viva 123, Springfield',
    'telefono': '+593 99 999 9999',
    'email': 'contacto@farmaciahealthy.com'
}

productos_list = [
    {'codigo': 'P001', 'nombre': 'Paracetamol', 'descripcion': 'Medicamento para el dolor', 'iva': 'SI', 'stock': 100, 'precio': 2.50},
    {'codigo': 'P002', 'nombre': 'Ibuprofeno', 'descripcion': 'Anti-inflamatorio', 'iva': 'SI', 'stock': 75, 'precio': 3.00},
    {'codigo': 'P003', 'nombre': 'Jarabe para la tos', 'descripcion': 'Medicamento para la tos', 'iva': 'SI', 'stock': 50, 'precio': 4.00},
    {'codigo': 'P004', 'nombre': 'Vitamina C', 'descripcion': 'Suplemento vitamínico', 'iva': 'SI', 'stock': 200, 'precio': 1.00},
    {'codigo': 'P005', 'nombre': 'Alcohol en gel', 'descripcion': 'Desinfectante de manos', 'iva': 'NO', 'stock': 150, 'precio': 2.00},
    {'codigo': 'P006', 'nombre': 'Amoxicilina', 'descripcion': 'Antibiótico', 'iva': 'SI', 'stock': 120, 'precio': 3.50},
    {'codigo': 'P007', 'nombre': 'Parche para el dolor', 'descripcion': 'Alivio muscular', 'iva': 'NO', 'stock': 80, 'precio': 1.50},
    {'codigo': 'P008', 'nombre': 'Gasa estéril', 'descripcion': 'Material médico', 'iva': 'NO', 'stock': 500, 'precio': 0.50},
]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/nosotros')
def nosotros():
    return render_template('paginadenosotros.html', empresa=empresa)

@app.route('/clientes')
def clientes():
    return render_template('paginalistadodeclientes.html')

@app.route('/productos')
def productos():
    return render_template('paginadelistadodeproductos.html', productos=productos_list)

@app.route('/editar_productos', methods=['GET', 'POST'])
def editar_productos():
    if request.method == 'POST':
        nuevo_producto = {
            'codigo': request.form['codigo'],
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'iva': request.form['iva'],
            'stock': int(request.form['stock']),
            'precio': float(request.form['precio'])
        }
        productos_list.append(nuevo_producto)
        return redirect(url_for('productos'))
    
    return render_template('editar_productos.html')


@app.route('/promociones')
def promociones():
    return render_template('paginapromociones.html')

@app.route('/editar_empresa', methods=['GET', 'POST'])
def editar_empresa():
    if request.method == 'POST':
        empresa['mision'] = request.form['mision']
        empresa['vision'] = request.form['vision']
        empresa['direccion'] = request.form['direccion']
        empresa['telefono'] = request.form['telefono']
        empresa['email'] = request.form['email']
        
        return redirect(url_for('nosotros'))
    
    return render_template('editar_empresa.html', empresa=empresa)


if __name__ == '__main__':
    app.run(debug=True)
