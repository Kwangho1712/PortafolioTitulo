CREATE TABLE cliente (
    run             VARCHAR2(12) NOT NULL,
    nombre          VARCHAR2(99) NOT NULL,
    edad            INTEGER,
    fiar            VARCHAR2(5) NOT NULL,
    fiado_id_fiado  NUMBER
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( run );

CREATE TABLE familia_producto (
    id_familia_producto   NUMBER GENERATED by default on null as IDENTITY,
    dsc_familia_producto  VARCHAR2(999)
);

ALTER TABLE familia_producto ADD CONSTRAINT familia_producto_pk PRIMARY KEY ( id_familia_producto );

CREATE TABLE producto (
    cod_producto                          INTEGER NOT NULL,
    nombre                                VARCHAR2(50) NOT NULL,
    descripcion                           VARCHAR2(100) NOT NULL,
    precio_compra                         NUMBER NOT NULL,
    precio_venta                          NUMBER NOT NULL,
    tipo_prod_id_tipo_prod                NUMBER NOT NULL, 
    fam_prod_id_fam_prod                  NUMBER NOT NULL,
    stock_actual                          NUMBER NOT NULL,
    stock_critico                         NUMBER NOT NULL
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( cod_producto );

CREATE TABLE proveedor (
    rut        VARCHAR2(12) NOT NULL,
    nombre     VARCHAR2(99) NOT NULL,
    telefono   VARCHAR2(13),
    email      VARCHAR2(99),
    direccion  VARCHAR2(60),
    rubro      VARCHAR2(90)
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( rut );

CREATE TABLE tipo_producto (
    id_tipo_producto   NUMBER GENERATED by default on null as IDENTITY,
    dsc_tipo_producto  VARCHAR2(999)
);

ALTER TABLE tipo_producto ADD CONSTRAINT tipo_producto_pk PRIMARY KEY ( id_tipo_producto );

CREATE TABLE fiado (
    id_fiado     NUMBER GENERATED by default on null as IDENTITY,
    monto_fiado  NUMBER,
    fecha_fiado  DATE
);

ALTER TABLE fiado ADD CONSTRAINT fiado_pk PRIMARY KEY ( id_fiado );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_fiado_fk FOREIGN KEY ( fiado_id_fiado )
        REFERENCES fiado ( id_fiado );

ALTER TABLE producto
    ADD CONSTRAINT prod_fam_prod_fk FOREIGN KEY ( fam_prod_id_fam_prod )
        REFERENCES familia_producto ( id_familia_producto );

ALTER TABLE producto
    ADD CONSTRAINT producto_tipo_producto_fk FOREIGN KEY ( tipo_prod_id_tipo_prod )
        REFERENCES tipo_producto ( id_tipo_producto );